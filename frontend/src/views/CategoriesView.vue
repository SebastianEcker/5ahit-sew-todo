<template>
    <div class="row d-flex justify-content-center mx-auto mt-5">
        <div class="col-6 pt-6">
            <button @click="openPopup" class="btn btn-primary mb-3">Create Category</button>
            <table class="table">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">Name</th>
                    <th scope="col">Farbe</th>
                    <th scope="col">Aktionen</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="(category, idx) in categoryList" :key="idx">
                    <th scope="row">{{ idx + 1 }}</th>
                    <td>{{ category.name }}</td>
                    <td :style="{ color: category.color }">{{ category.color }}</td>
                    <td>
                        <button class="mr-1 btn btn-secondary" @click="openEditPopup(category)">Bearbeiten</button>
                        <button class="btn btn-danger" @click="removeCategory(category.id)">Löschen</button>
                    </td>
                </tr>
            </tbody>
        </table>
        </div>
    </div>
    <CategoryPopup 
        v-if="showPopup" 
        :isEditMode="isEditMode" 
        :initialCategory="selectedCategory" 
        @close="showPopup = false" 
        @category-created="fetchCategories" 
        @category-updated="fetchCategories" 
    />
</template>
  
<script setup>
import { getCategoriesByUser, deleteCategory } from '../api/category';
import { ref, onMounted } from 'vue';
import CategoryPopup from '../components/CategoryPopup.vue';

const categoryList = ref([]);
const showPopup = ref(false);
const isEditMode = ref(false);
const selectedCategory = ref({ name: '', color: '#000000' });

const fetchCategories = async () => {
    const categoryResponse = await getCategoriesByUser();
    categoryList.value = categoryResponse.data;
    console.log(categoryList.value);
};

const openPopup = () => {
    isEditMode.value = false;
    selectedCategory.value = { name: '', color: '#000000' };
    showPopup.value = true;
};

const openEditPopup = (category) => {
    isEditMode.value = true;
    selectedCategory.value = { ...category };
    showPopup.value = true;
};

const removeCategory = async (categoryId) => {
    await deleteCategory(categoryId);
    fetchCategories();
};

onMounted(fetchCategories);

</script>