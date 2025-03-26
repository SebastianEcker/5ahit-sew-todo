<template>
  <div class="filter-dropdown">
    <button @click="toggleFilters" class="filter-button">
      <Filter class="filter-icon" /> Filter
    </button>
    
    <transition name="fade">
      <div v-if="showFilters" class="filter-dropdown-menu">
        <div class="filter-header">
          <h3 class="filter-title">Filter</h3>
          <button @click="closeFilters" class="close-button">
            <span aria-hidden="true">&times;</span>
          </button>
        </div>
        
        <div class="filter-grid">
          <div class="filter-item">
            <label class="filter-label">Sortierung nach Name</label>
            <select v-model="filters.sort_by_name" class="filter-select">
              <option value="asc">Aufsteigend</option>
              <option value="desc">Absteigend</option>
            </select>
          </div>
          
          <div class="filter-item">
            <label class="filter-label">Anzahl der Kategorien</label>
            <input type="number" v-model.number="filters.limit" class="filter-input" min="1">
          </div>
        </div>
        
        <div class="filter-actions">
          <button @click="resetFilters" class="reset-button">Zurücksetzen</button>
          <button @click="applyFilters" class="apply-button">Anwenden</button>
        </div>
      </div>
    </transition>
    
    <transition name="fade">
      <div v-if="showFilters" class="filter-backdrop" @click="closeFilters"></div>
    </transition>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue';
import { Filter } from 'lucide-vue-next';

const emit = defineEmits(['filter-applied']);

const showFilters = ref(false);

const defaultFilters = {
  skip: 0,
  limit: 1000,
  sort_by_name: 'asc'
};

const filters = reactive({ ...defaultFilters });

const toggleFilters = () => {
  showFilters.value = !showFilters.value;
};

const closeFilters = () => {
  showFilters.value = false;
};

const applyFilters = () => {
  emit('filter-applied', { ...filters });
  closeFilters();
};

const resetFilters = () => {
  Object.keys(defaultFilters).forEach(key => {
    filters[key] = defaultFilters[key];
  });
  applyFilters();
};
</script>

<style scoped>
.filter-dropdown {
  position: relative;
}

.filter-button {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1rem;
  background-color: white;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  font-weight: 500;
  transition: all 0.2s;
}

.filter-button:hover {
  background-color: #f8fafc;
  border-color: #cbd5e1;
}

.filter-icon {
  width: 1rem;
  height: 1rem;
}

.filter-dropdown-menu {
  position: absolute;
  top: calc(100% + 0.5rem);
  right: 0;
  z-index: 1000;
  width: 400px;
  max-width: 90vw;
  background-color: white;
  border-radius: 0.5rem;
  box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  overflow: hidden;
}

.filter-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 1rem;
  border-bottom: 1px solid #e2e8f0;
}

.filter-title {
  font-size: 1.125rem;
  font-weight: 600;
  margin: 0;
}

.close-button {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 2rem;
  height: 2rem;
  border-radius: 9999px;
  border: none;
  background: transparent;
  cursor: pointer;
  font-size: 1.5rem;
}

.close-button:hover {
  background-color: #f1f5f9;
}

.filter-grid {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  padding: 1rem;
}

.filter-item {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.filter-label {
  font-size: 0.875rem;
  font-weight: 500;
  color: #64748b;
}

.filter-select,
.filter-input {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  background-color: white;
  font-size: 0.875rem;
}

.filter-select:focus,
.filter-input:focus {
  outline: none;
  border-color: #94a3b8;
  box-shadow: 0 0 0 1px #94a3b8;
}

.filter-actions {
  display: flex;
  justify-content: flex-end;
  gap: 0.5rem;
  padding: 1rem;
  border-top: 1px solid #e2e8f0;
}

.reset-button {
  padding: 0.5rem 1rem;
  background-color: white;
  border: 1px solid #e2e8f0;
  border-radius: 0.375rem;
  font-weight: 500;
  transition: all 0.2s;
}

.reset-button:hover {
  background-color: #f8fafc;
  border-color: #cbd5e1;
}

.apply-button {
  padding: 0.5rem 1rem;
  background-color: #3b82f6;
  color: white;
  border: none;
  border-radius: 0.375rem;
  font-weight: 500;
  transition: all 0.2s;
}

.apply-button:hover {
  background-color: #2563eb;
}

.filter-backdrop {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 999;
  background-color: rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(2px);
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease, transform 0.2s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
  transform: translateY(-10px);
}
</style>
