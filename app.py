import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
import os
from datetime import datetime

# Page config
st.set_page_config(page_title="Cloud Task Scheduling", layout="wide")

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: #f0f2f6;
        padding: 1rem;
        border-radius: 10px;
        border-left: 4px solid #1f77b4;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)

class Processor:
    def __init__(self, processor_id, processing_power=1.0):
        self.id = processor_id
        self.processing_power = processing_power
        self.current_time = 0
        self.assigned_tasks = []  # Store task objects directly
    
    def assign_task(self, task, arrival_time):
        start_time = max(self.current_time, arrival_time)
        processing_time = task.execution_time / self.processing_power
        finish_time = start_time + processing_time
        
        # Store the task object and its calculated times
        task_info = {
            'task': task,
            'start_time': start_time,
            'finish_time': finish_time,
            'execution_time': task.execution_time  # Store execution time here
        }
        self.assigned_tasks.append(task_info)
        self.current_time = finish_time
        return finish_time

class DataCenter:
    def __init__(self, num_processors=4):
        self.processors = [Processor(i) for i in range(num_processors)]
    
    def reset_processors(self):
        for processor in self.processors:
            processor.current_time = 0
            processor.assigned_tasks = []

class Task:
    def __init__(self, task_id, arrival_time, execution_time):
        self.id = task_id
        self.arrival_time = arrival_time
        self.execution_time = execution_time

class TaskScheduler:
    def __init__(self, datacenter):
        self.datacenter = datacenter
        self.tasks = []
    
    def load_tasks(self, num_tasks):
        self.tasks = []
        np.random.seed(42)
        
        # Generate arrival times
        arrival_times = np.cumsum(np.random.exponential(50, num_tasks))
        arrival_times = np.maximum(arrival_times, 0)  # Ensure non-negative
        
        # Generate execution times
        execution_times = np.random.exponential(100, num_tasks) + 10
        
        for i in range(num_tasks):
            self.tasks.append(Task(i, arrival_times[i], execution_times[i]))
    
    def fcfs_schedule(self):
        """First-Come-First-Served scheduling"""
        self.datacenter.reset_processors()
        finish_times = []
        
        # Sort by arrival time
        sorted_tasks = sorted(self.tasks, key=lambda x: x.arrival_time)
        
        for task in sorted_tasks:
            # Find processor with earliest available time
            best_processor = min(self.datacenter.processors, key=lambda p: p.current_time)
            finish_time = best_processor.assign_task(task, task.arrival_time)
            finish_times.append(finish_time)
        
        return finish_times
    
    def sjf_schedule(self):
        """Shortest Job First scheduling"""
        self.datacenter.reset_processors()
        finish_times = []
        
        # Sort by execution time (shortest first)
        sorted_tasks = sorted(self.tasks, key=lambda x: x.execution_time)
        
        for task in sorted_tasks:
            # Find processor with earliest available time
            best_processor = min(self.datacenter.processors, key=lambda p: p.current_time)
            finish_time = best_processor.assign_task(task, task.arrival_time)
            finish_times.append(finish_time)
        
        return finish_times
    
    def eft_schedule(self):
        """Earliest Finish Time scheduling"""
        self.datacenter.reset_processors()
        finish_times = []
        
        for task in self.tasks:
            # Calculate possible finish times on all processors
            possible_finish_times = []
            for processor in self.datacenter.processors:
                start_time = max(processor.current_time, task.arrival_time)
                processing_time = task.execution_time / processor.processing_power
                finish_time = start_time + processing_time
                possible_finish_times.append((finish_time, processor))
            
            # Choose processor with earliest finish time
            best_finish_time, best_processor = min(possible_finish_times, key=lambda x: x[0])
            actual_finish_time = best_processor.assign_task(task, task.arrival_time)
            finish_times.append(actual_finish_time)
        
        return finish_times

def calculate_metrics(datacenter, finish_times, tasks):
    """Calculate performance metrics"""
    if not finish_times:
        return {
            'makespan': 0,
            'throughput': 0,
            'resource_utilization': 0
        }
    
    makespan = max(finish_times)
    throughput = len(tasks) / makespan if makespan > 0 else 0
    
    # Calculate utilization for each processor
    utilizations = []
    for processor in datacenter.processors:
        if makespan > 0:
            # Sum execution times from stored task info
            busy_time = sum(task_info['execution_time'] for task_info in processor.assigned_tasks)
            utilization = (busy_time / makespan) * 100
        else:
            utilization = 0
        utilizations.append(utilization)
    
    return {
        'makespan': makespan,
        'throughput': throughput,
        'resource_utilization': np.mean(utilizations)
    }

def main():
    st.markdown('<h1 class="main-header">☁️ Cloud Task Scheduling Simulator</h1>', unsafe_allow_html=True)
    
    # Sidebar controls
    with st.sidebar:
        st.header("🎯 Simulation Controls")
        
        num_tasks = st.selectbox(
            "Number of Tasks",
            options=[100, 200, 300, 400, 500],
            index=0
        )
        
        st.subheader("Scheduling Algorithms")
        fcfs = st.checkbox("FCFS (First-Come-First-Served)", value=True)
        sjf = st.checkbox("SJF (Shortest Job First)", value=True)
        eft = st.checkbox("EFT (Earliest Finish Time)", value=True)
        
        run_btn = st.button("🚀 Run Simulation", type="primary", use_container_width=True)
    
    # Main content
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📊 About This Simulator")
        st.info("""
        This tool simulates different cloud task scheduling algorithms:
        - **FCFS**: Tasks are processed in order of arrival
        - **SJF**: Shortest tasks are processed first  
        - **EFT**: Tasks are assigned to processors for earliest completion
        """)
    
    with col2:
        st.subheader("📈 Metrics Calculated")
        st.write("""
        - **Makespan**: Total completion time
        - **Throughput**: Tasks per second
        - **Utilization**: CPU usage efficiency
        """)
    
    if run_btn:
        # Get selected algorithms
        algorithms = []
        if fcfs: algorithms.append("FCFS")
        if sjf: algorithms.append("SJF") 
        if eft: algorithms.append("EFT")
        
        if not algorithms:
            st.error("⚠️ Please select at least one algorithm!")
            return
        
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        results = {}
        
        for i, algo in enumerate(algorithms):
            status_text.text(f"🔄 Running {algo} algorithm...")
            progress_bar.progress((i + 1) / len(algorithms))
            
            try:
                datacenter = DataCenter()
                scheduler = TaskScheduler(datacenter)
                scheduler.load_tasks(num_tasks)
                
                if algo == "FCFS":
                    finish_times = scheduler.fcfs_schedule()
                elif algo == "SJF":
                    finish_times = scheduler.sjf_schedule()
                elif algo == "EFT":
                    finish_times = scheduler.eft_schedule()
                
                results[algo] = calculate_metrics(datacenter, finish_times, scheduler.tasks)
                time.sleep(0.5)  # Small delay for better UX
                
            except Exception as e:
                st.error(f"Error in {algo}: {str(e)}")
                continue
        
        status_text.text("✅ Simulation completed!")
        progress_bar.progress(100)
        time.sleep(0.5)
        
        # Clear progress indicators
        status_text.empty()
        progress_bar.empty()
        
        if results:
            # Display results
            st.markdown("---")
            st.header("📋 Simulation Results")
            
            # Metrics cards
            st.subheader(f"Performance for {num_tasks} Tasks")
            cols = st.columns(len(algorithms))
            
            for idx, algo in enumerate(algorithms):
                with cols[idx]:
                    if algo in results:
                        st.markdown(f'<div class="metric-card">', unsafe_allow_html=True)
                        st.subheader(algo)
                        st.metric("Makespan", f"{results[algo]['makespan']:.2f}s")
                        st.metric("Throughput", f"{results[algo]['throughput']:.4f}")
                        st.metric("Utilization", f"{results[algo]['resource_utilization']:.2f}%")
                        st.markdown('</div>', unsafe_allow_html=True)
            
            # Visualization
            st.subheader("📊 Performance Comparison")
            
            if len(results) > 0:
                fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 4))
                
                algorithms_list = list(results.keys())
                makespans = [results[algo]['makespan'] for algo in algorithms_list]
                throughputs = [results[algo]['throughput'] for algo in algorithms_list]
                utilizations = [results[algo]['resource_utilization'] for algo in algorithms_list]
                
                colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
                
                ax1.bar(algorithms_list, makespans, color=colors[:len(algorithms_list)], alpha=0.8)
                ax1.set_title('Makespan Comparison')
                ax1.set_ylabel('Seconds')
                
                ax2.bar(algorithms_list, throughputs, color=colors[:len(algorithms_list)], alpha=0.8)
                ax2.set_title('Throughput Comparison')
                ax2.set_ylabel('Tasks/Second')
                
                ax3.bar(algorithms_list, utilizations, color=colors[:len(algorithms_list)], alpha=0.8)
                ax3.set_title('Utilization Comparison')
                ax3.set_ylabel('Percentage (%)')
                
                plt.tight_layout()
                st.pyplot(fig)
            
            # Download results
            st.subheader("💾 Export Results")
            results_df = pd.DataFrame([
                {
                    'Algorithm': algo,
                    'Makespan (seconds)': metrics['makespan'],
                    'Throughput (tasks/second)': metrics['throughput'],
                    'Utilization (%)': metrics['resource_utilization']
                }
                for algo, metrics in results.items()
            ])
            
            st.dataframe(results_df, use_container_width=True)
            
            csv = results_df.to_csv(index=False)
            st.download_button(
                label="📥 Download CSV",
                data=csv,
                file_name=f"cloud_scheduling_{num_tasks}_tasks.csv",
                mime="text/csv"
            )
            
            # Best algorithm recommendation
            if results:
                best_algo = min(results.keys(), key=lambda x: results[x]['makespan'])
                st.success(f"🎯 **Best performing algorithm: {best_algo}** (lowest makespan)")

if __name__ == "__main__":
    main()