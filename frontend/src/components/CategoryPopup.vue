<template>
    <div class="modal-backdrop" @click.self="closePopup">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">{{ isEditMode ? 'Kategorien aktualisieren' : 'Kategorien erstellen' }}</h5>
                    <button type="button" class="close" @click="closePopup" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <form @submit.prevent="submitForm">
                        <div class="mb-3">
                            <label for="name" class="form-label">Name</label>
                            <input v-model="category.name" type="text" id="name" class="form-control" required />
                        </div>
                        <div class="mb-3">
                            <label for="color" class="form-label">Farbe</label>
                            <input v-model="category.color" type="color" id="color" class="form-control" required />
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
import { createCategory, updateCategory } from '../api/category';
import { ref, watch } from 'vue';

const props = defineProps({
    isEditMode: Boolean,
    initialCategory: {
        type: Object,
        default: () => ({ name: '', color: '#000000' })
    }
});

const emit = defineEmits(['close', 'category-updated', 'category-created']);

const category = ref({ ...props.initialCategory });

watch(() => props.initialCategory, (newVal) => {
    category.value = { ...newVal };
});

const submitForm = async () => {
    if (props.isEditMode) {
        await updateCategory(category.value.id, category.value);
        emit('category-updated');
    } else {
        await createCategory(category.value);
        emit('category-created');
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