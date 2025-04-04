import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ProfileView from '../views/ProfileView.vue'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import LogoutView from '../views/LogoutView.vue'
import RefreshView from '../views/RefreshView.vue'
import { useAuthStore } from '../store/auth'
import CategoriesView from '../views/CategoriesView.vue'
import UserView from '../views/UserView.vue'

const routes = [
    {
        path: '/',
        name: 'Home',
        component: HomeView,
    },
    {
        path: '/register',
        name: 'Register',
        component: RegisterView,
    },
    {
        path: '/login',
        name: 'Login',
        component: LoginView,
    },
    {
        path: '/profile',
        name: 'Profile',
        component: ProfileView,
        meta: { requiresAuth: true },
    },
    {
        path: '/categories',
        name: 'Categories',
        component: CategoriesView,
        meta: { requiresAuth: true },
    },
    {
        path: '/users',
        name: 'Users',
        component: UserView,
        meta: { requiresAuth: true },

    },
    {
        path: '/logout',
        name: 'Logout',
        component: LogoutView,
    },
    {
        path: '/refresh',
        name: 'Refresh',
        component: RefreshView,
    },
]

const router = createRouter({
    history: createWebHistory(),
    routes, // short for `routes: routes`
})

router.beforeEach((to, from , next) => {
    const auth = useAuthStore();
    if (to.matched.some((record) => record.meta.requiresAuth)) {
        if (auth.isAuthenticated) {
            next();
            return;
        }
        next("/login");
    } else {
        next();
    }

})

export default router;