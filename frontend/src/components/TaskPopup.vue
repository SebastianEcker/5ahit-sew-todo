<template>
    <div class="modal fade show d-block" tabindex="-1" role="dialog">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">{{ isEditMode ? 'Edit Task' : 'Create Task' }}</h5>
                    <button type="button" class="close" @click="closePopup" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <form @submit.prevent="submitForm">
                        <div class="mb-3">
                            <label for="title" class="form-label">Title</label>
                            <input v-model="task.title" type="text" id="title" class="form-control" required />
                        </div>
                        <div class="mb-3">
                            <label for="description" class="form-label">Description</label>
                            <textarea v-model="task.description" id="description" class="form-control" required></textarea>
                        </div>
                        <div class="mb-3">
                            <label for="end_date" class="form-label">End Date</label>
                            <input v-model="task.end_date" type="date" id="end_date" class="form-control" required />
                        </div>
                        <div class="mb-3">
                            <label for="completed" class="form-label">Completed</label>
                            <input v-model="task.completed" type="checkbox" id="completed" class="form-check-input" />
                        </div>
                        <div class="mb-3">
                            <label for="category" class="form-label">Category</label>
                            <select v-model="task.category_id" id="category" class="form-control" required>
                                <option v-for="category in categories" :key="category.id" :value="category.id">
                                    {{ category.name }}
                                </option>
                            </select>
                        </div>
                        <div class="modal-footer">
                            <button type="submit" class="btn btn-primary">{{ isEditMode ? 'Update' : 'Create' }}</button>
                            <button type="button" class="btn btn-secondary" @click="closePopup">Cancel</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>
</template>
  
<script setup>
import { createTask, updateTask } from '../api/task';
import { ref, watch } from 'vue';

const props = defineProps({
    isEditMode: Boolean,
    initialTask: {
        type: Object,
        default: () => ({ title: '', description: '', end_date: '', completed: false, category_id: null })
    },
    categories: {
        type: Array,
        default: () => []
    }
});

const emit = defineEmits(['close', 'task-updated', 'task-created']);

const task = ref({ ...props.initialTask });

watch(() => props.initialTask, (newVal) => {
    task.value = { ...newVal };
});

const submitForm = async () => {
    if (props.isEditMode) {
        await updateTask(task.value.id, task.value);
        emit('task-updated');
    } else {
        await createTask(task.value);
        emit('task-created');
    }
    closePopup();
};

const closePopup = () => {
    emit('close');
};
</script>
