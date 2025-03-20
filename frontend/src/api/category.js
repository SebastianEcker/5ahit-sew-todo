import request from './req';

export const getCategories = (params) => request('GET', '/categories', { params });
export const getCategoriesByUser = (params) => request('GET', `/categories/user?${params}`);
export const getCategoryById = (categoryId) => request('GET', `/categories/${categoryId}`);
export const createCategory = (category) => request('POST', '/categories', category);
export const updateCategory = (categoryId, category) => request('PUT', `/categories/${categoryId}`, category);
export const deleteCategory = (categoryId) => request('DELETE', `/categories/${categoryId}`);