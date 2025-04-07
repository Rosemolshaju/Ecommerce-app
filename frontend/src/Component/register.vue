<template>
  <div class="registration-form max-w-md mx-auto">
    <form @submit.prevent="register" class="bg-white p-6 rounded shadow-md">
      <input 
        type="text" 
        v-model="username" 
        placeholder="Username" 
        class="block w-full mb-4 p-2 border rounded" 
      />
      <input 
        type="email" 
        v-model="email" 
        placeholder="Email" 
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
        Register
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
      email: "",
      password: "",
    };
  },
  methods: {
    async register() {
      try {
        await api.post("/users/register", { username: this.username, email: this.email, password: this.password });
        alert("Registration successful!");
      } catch (error) {
        console.error("Registration failed:", error);
      }
    },
  },
};
</script>
