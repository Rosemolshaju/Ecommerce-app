<template>
  <div class="login-form max-w-md mx-auto">
    <form @submit.prevent="login" class="bg-white p-6 rounded shadow-md">
      <input 
        type="text" 
        v-model="username" 
        placeholder="Username" 
        class="block w-full mb-4 p-2 border rounded" 
      />
      <input 
        type="password" 
        v-model="password" 
        placeholder="Password" 
        class="block w-full mb-4 p-2 border rounded" 
      />
      <button 
        type="submit" 
        class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
        Login
      </button>
    </form>
  </div>
</template>

<script>
import api from "../utils/api";

export default {
  data() {
    return {
      username: "",
      password: "",
    };
  },
  methods: {
    async login() {
      try {
        const response = await api.post("/users/login", { username: this.username, password: this.password });
        localStorage.setItem("token", response.data.token);
        alert("Login successful!");
      } catch (error) {
        console.error("Login failed:", error);
      }
    },
  },
};
</script>
