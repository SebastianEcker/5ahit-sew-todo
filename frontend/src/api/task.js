import request from './req';



export const getTasks = (params) => request('GET', '/tasks', { params });
export const getTasksByUser = (params) => request('GET', `/tasks/user?${params}`);
export const getTaskById = (taskId) => request('GET', `/tasks/${taskId}`);
export const createTask = (task) => request('POST', '/tasks', task);
export const updateTask = (taskId, task) => request('PUT', `/tasks/${taskId}`, task);
export const updateTaskCompleted = (taskId) => request('PUT', `/tasks/completed/${taskId}`);
export const deleteTask = (taskId) => request('DELETE', `/tasks/${taskId}`);




