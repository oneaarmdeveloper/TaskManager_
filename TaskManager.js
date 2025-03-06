import React, { useState, useEffect } from "react";
import axios from "axios";

function TaskManager() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState("");

  // Fetch tasks from backend when component loads
  useEffect(() => {
    axios.get("http://127.0.0.1:5000/tasks")
      .then((response) => setTasks(response.data))
      .catch((error) => console.error("Error fetching tasks:", error));
  }, []);

  // Function to add a task
  const addTask = () => {
    axios.post("http://127.0.0.1:5000/tasks", { task: newTask })
      .then(() => {
        setTasks([...tasks, { task: newTask, time: new Date().toLocaleTimeString() }]);
        setNewTask("");
      })
      .catch((error) => console.error("Error adding task:", error));
  };

  return (
    <div>
      <h2>Task Manager</h2>
      <input
        type="text"
        placeholder="Enter task"
        value={newTask}
        onChange={(e) => setNewTask(e.target.value)}
      />
      <button onClick={addTask}>Add Task</button>

      <h3>Tasks:</h3>
      <ul>
        {tasks.map((task, index) => (
          <li key={index}>{task.task} (Added at: {task.time})</li>
        ))}
      </ul>
    </div>
  );
}

export default TaskManager;
