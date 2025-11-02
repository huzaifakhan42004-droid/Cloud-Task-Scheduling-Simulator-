# Cloud Task Scheduling Simulator

A sophisticated web-based simulation platform built with Streamlit that enables comprehensive analysis and visualization of task scheduling algorithms in cloud computing environments.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)

## 📊 Live Demo
**Experience the simulator now:** [https://btqf4d9mzj4vq4aivwuwd5.streamlit.app/]

## 🎯 Overview

This interactive web application provides researchers, students, and cloud engineers with a powerful tool to simulate, analyze, and compare various task scheduling algorithms. Gain deep insights into performance metrics and optimize your cloud resource allocation strategies.

## ✨ Key Features

### 🎮 Interactive Simulation
- **Real-time Algorithm Comparison** - Side-by-side performance analysis
- **Dynamic Parameter Tuning** - Adjust task counts, VM configurations on-the-fly
- **Live Visualization** - Watch scheduling unfold with interactive charts

### 📈 Advanced Analytics
- **Comprehensive Metrics** - Makespan, Throughput, Resource Utilization, Cost Analysis
- **Performance Benchmarking** - Compare multiple algorithms simultaneously
- **Statistical Insights** - Detailed breakdown of scheduling efficiency

### 🔧 Technical Capabilities
- **Multiple Scheduling Algorithms** - FCFS, SJF, Priority, Round Robin, Min-Min, Max-Min
- **Custom Workload Generation** - Flexible task creation with varied requirements
- **Heterogeneous VM Support** - Simulate real-world cloud environments

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- pip package manager

### Installation & Run

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/cloud-task-scheduling-simulator.git
   cd cloud-task-scheduling-simulator
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Application**
   ```bash
   streamlit run app.py
   ```

4. **Access the Simulator**
   - Open your browser to `http://localhost:8501`
   - Start simulating immediately!

## 🎮 How to Use

### 1. **Configure Simulation**
- Set number of tasks and virtual machines
- Define task characteristics (execution time, priority)
- Configure VM specifications (processing power, cost)

### 2. **Select Algorithms**
- Choose from multiple scheduling strategies
- Compare 2+ algorithms simultaneously
- Customize algorithm parameters

### 3. **Run & Analyze**
- Execute simulation with one click
- View real-time Gantt charts and metrics
- Export results for further analysis

## 📊 Supported Algorithms

| Algorithm | Type | Best For |
|-----------|------|----------|
| **FCFS** | Basic | Simple workloads |
| **SJF** | Optimized | Throughput maximization |
| **Priority** | Priority-based | Mission-critical tasks |
| **Round Robin** | Time-slicing | Fair resource sharing |
| **Min-Min** | Cloud-optimized | Quick task completion |
| **Max-Min** | Cloud-optimized | Resource utilization |

## 🏗️ Architecture

```
application/
├── app.py                 # Main Streamlit application
├── scheduler/            # Scheduling algorithms
│   ├── fcfs.py
│   ├── sjf.py
│   ├── priority.py
│   └── cloud_algorithms.py
├── utils/
│   ├── data_generator.py # Task/VM generation
│   ├── visualizer.py     # Chart plotting functions
│   └── metrics.py        # Performance calculations
└── assets/              # Static files
```

## 📈 Sample Output

### Performance Metrics Dashboard
- **Makespan Comparison** across algorithms
- **Resource Utilization** heatmaps
- **Cost Analysis** breakdowns
- **Throughput** over time charts

### Visualization Features
- Interactive Gantt charts
- Real-time metric updates
- Comparative analysis graphs
- Exportable results

## 🛠️ Technical Stack

- **Frontend**: Streamlit
- **Backend**: Python 3.8+
- **Data Processing**: Pandas, NumPy
- **Visualization**: Plotly, Matplotlib
- **Deployment**: Streamlit Sharing (optional)

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

1. **Report Bugs** - Open an issue with detailed description
2. **Suggest Features** - Share your ideas for improvements
3. **Submit Pull Requests** - Implement new algorithms or enhancements

### Development Setup
```bash
# Fork and clone the repository
git clone https://github.com/your-username/cloud-task-scheduling-simulator.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@your-username](https://github.com/your-username)
- LinkedIn: [Your Profile](https://linkedin.com/in/your-profile)

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Icons from [Font Awesome](https://fontawesome.com)
- Inspired by cloud computing research and educational materials

---

**⭐ If you find this project helpful, please give it a star on GitHub!**

---
