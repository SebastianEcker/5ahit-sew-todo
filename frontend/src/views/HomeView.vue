<template>
    <div class="row d-flex justify-content-center mx-auto mt-5">
        <div class="col-6 pt-6">
            <div class="d-flex justify-content-between mb-3">
                <button @click="openCreatePopup" class="btn btn-primary">Create Task</button>
            </div>
            <table class="table">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Titel</th>
                    <th scope="col">Beschreibung</th>
                    <th scope="col">End Datum</th>
                    <th scope="col">Erledigt</th>
                    <th scope="col">Kategorie</th>
                    <th scope="col">Aktionen</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(task, idx) in taskList" :key="idx">
                    <th scope="row">{{ idx + 1 }}</th>
                    <td>{{ task.title }}</td>
                    <td>{{ task.description }}</td>
                    <td>{{ task.end_date }}</td>
                    <td>{{ task.completed }}</td>
                    <td>{{ task.category.name }}</td>
                    <td>
                        <button class="mr-1 btn btn-secondary" @click="openEditPopup(task)">Bearbeiten</button>
                        <button class="btn btn-danger" @click="removeTask(task.id)">Löschen</button>
                    </td>
                </tr>
            </tbody>
        </table>
        </div>
    </div>
    <TaskPopup 
        v-if="showPopup" 
        :isEditMode="isEditMode" 
        :initialTask="selectedTask" 
        :categories="categories"
        @close="showPopup = false" 
        @task-created="fetchTasks" 
        @task-updated="fetchTasks" 
    />
</template>
  
<script setup>
import { getTasksByUser, deleteTask } from '../api/task';
import { getCategoriesByUser } from '../api/category';
import { ref, onMounted } from 'vue';
import TaskPopup from '../components/TaskPopup.vue';

const taskList = ref([]);
const categories = ref([]);
const showPopup = ref(false);
const isEditMode = ref(false);
const selectedTask = ref({ 
    title: '', 
    description: '',
    end_date: '',
    completed: false,
    category_id: null
});

const currentFilters = ref({
  skip: 0,
  limit: 1000,
  category_ids: [],
  end_date: null,
  completed: null,
  sort_by_end_date: 'asc'
});

const fetchTasks = async (params = {}) => {
    const taskResponse = await getTasksByUser(params);
    taskList.value = taskResponse.data;
    console.log(taskList.value);
};

const fetchCategories = async () => {
    const categoryResponse = await getCategoriesByUser();
    categories.value = categoryResponse.data;
    console.log(categories.value);
};

const openCreatePopup = () => {
    isEditMode.value = false;
    selectedTask.value = { title: '', description: '', end_date: '', completed: false, category_id: null };
    showPopup.value = true;
};

const openEditPopup = (task) => {
    isEditMode.value = true;
    selectedTask.value = { ...task };
    showPopup.value = true;
};

const removeTask = async (taskId) => {
    await deleteTask(taskId);
    fetchTasks();
};

const formatParams = (params) => {
    const searchParams = new URLSearchParams();
    Object.entries(params).forEach(([key, value]) => {
        if (Array.isArray(value)) {
            value.forEach((val) => searchParams.append(key, val));
        } else if (value !== null && value !== undefined) {
            searchParams.append(key, value);
        }
    });
    return searchParams.toString();
};

onMounted(async () => {
    await fetchCategories();
    await fetchTasks(formatParams(currentFilters.value));
});

</script>