<template>
  <div class="modal-backdrop" @click.self="closePopup">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">{{ isEditMode ? 'Aufgaben aktualisieren' : 'Aufgabe erstellen' }}</h5>
          <button type="button" class="close" @click="closePopup" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        <div class="modal-body">
          <form @submit.prevent="submitForm">
            <div class="mb-3">
              <label for="title" class="form-label">Titel</label>
              <input v-model="task.title" type="text" id="title" class="form-control" required />
            </div>
            <div class="mb-3">
              <label for="description" class="form-label">Beschreibung</label>
              <textarea v-model="task.description" id="description" class="form-control" required></textarea>
            </div>
            <div class="mb-3">
              <label for="end_date" class="form-label">End Datum</label>
              <input v-model="task.end_date" type="date" id="end_date" class="form-control" required />
            </div>
            <div class="mb-3">
              <label for="category" class="form-label">Kategorien</label>
              <select v-model="task.category_id" id="category" class="form-control" required>
                <option v-for="category in categories" :key="category.id" :value="category.id">
                  {{ category.name }}
                </option>
              </select>
            </div>
            <div class="modal-footer">
              <button type="submit" class="btn btn-primary">{{ isEditMode ? 'Aktualisieren' : 'Erstellen' }}</button>
              <button type="button" class="btn btn-secondary" @click="closePopup">Abbrechen</button>
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
        default: () => ({ title: '', description: '', end_date: '', category_id: null })
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

<style scoped>
.modal-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  backdrop-filter: blur(1px);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1050;
}

.modal-dialog {
  max-width: 500px;
  width: 100%;
  margin: 1.75rem auto;
}

.modal-content {
  position: relative;
  display: flex;
  flex-direction: column;
  width: 100%;
  background-color: #fff;
  border-radius: 0.5rem;
  box-shadow: 0 0.5rem 1rem rgba(0, 0, 0, 0.15);
  padding: 1rem;
}

.modal-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem;
  border-bottom: 1px solid #dee2e6;
}

.modal-body {
  position: relative;
  flex: 1 1 auto;
  padding: 1rem;
}

.modal-footer {
  display: flex;
  justify-content: flex-end;
  padding: 1rem;
  border-top: 1px solid #dee2e6;
  gap: 0.5rem;
}

.close {
  background: transparent;
  border: 0;
  font-size: 1.5rem;
  cursor: pointer;
}

.form-label {
  margin-bottom: 0.5rem;
  display: inline-block;
}

.form-control {
  display: block;
  width: 100%;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  color: #495057;
  background-color: #fff;
  background-clip: padding-box;
  border: 1px solid #ced4da;
  border-radius: 0.25rem;
  transition: border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  margin-bottom: 0.5rem;
}

textarea.form-control {
  min-height: 100px;
}

.form-check-input {
  margin-left: 0.5rem;
}

.btn {
  display: inline-block;
  font-weight: 400;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  user-select: none;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: 0.25rem;
  transition: color 0.15s ease-in-out, background-color 0.15s ease-in-out, border-color 0.15s ease-in-out, box-shadow 0.15s ease-in-out;
  cursor: pointer;
}

.btn-primary {
  color: #fff;
  background-color: #007bff;
  border-color: #007bff;
}

.btn-secondary {
  color: #fff;
  background-color: #6c757d;
  border-color: #6c757d;
}

.mb-3 {
  margin-bottom: 1rem;
}
</style>