<template>
    <div class="modal fade show d-block" tabindex="-1" role="dialog">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">{{ isEditMode ? 'Edit Category' : 'Create Category' }}</h5>
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
                            <label for="color" class="form-label">Color</label>
                            <input v-model="category.color" type="color" id="color" class="form-control" required />
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
