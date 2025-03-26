<template>
  <div class="row d-flex justify-content-center mx-auto mt-5">
    <div class="col-6 pt-6">
      <div class="d-flex justify-content-between mb-3">
        <button @click="openPopup" class="btn btn-primary">Kategorie erstellen</button>
        <CategoryFilter @filter-applied="handleFilterApplied" />
      </div>
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
    @category-created="handleCategoryCreatedOrUpdated" 
    @category-updated="handleCategoryCreatedOrUpdated" 
  />
</template>
  
<script setup>
import { getCategoriesByUser, deleteCategory } from '../api/category';
import { ref, onMounted } from 'vue';
import CategoryPopup from '../components/CategoryPopup.vue';
import CategoryFilter from '../components/CategoryFilter.vue';

const categoryList = ref([]);
const showPopup = ref(false);
const isEditMode = ref(false);
const selectedCategory = ref({ name: '', color: '#000000' });

const currentFilters = ref({
  skip: 0,
  limit: 1000,
  sort_by_name: 'asc'
});

const fetchCategories = async (params = {}) => {
  const categoryResponse = await getCategoriesByUser(params);
  categoryList.value = categoryResponse.data;
  console.log(categoryList.value);
};

const handleFilterApplied = (filters) => {
  currentFilters.value = { ...filters };
  fetchCategories(formatParams(currentFilters.value));
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
  if (!confirm('Möchtest du diese Kategorie wirklich löschen?')) {
    return;
  }
  await deleteCategory(categoryId);
  await fetchCategories(formatParams(currentFilters.value));
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

const handleCategoryCreatedOrUpdated = () => {
  fetchCategories(formatParams(currentFilters.value));
  showPopup.value = false;
};

onMounted( (async () => {
  await fetchCategories(formatParams(currentFilters.value))
}));

</script>