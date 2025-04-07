<template>
  <div class="checkout max-w-3xl mx-auto mt-8">
    <h1 class="text-2xl font-bold mb-4">Order Summary</h1>
    <div v-for="item in cartItems" :key="item.id" class="border-b py-4">
      <div class="flex justify-between">
        <span>{{ item.name }} (x{{ item.quantity }})</span>
        <span>${{ item.price * item.quantity }}</span>
      </div>
    </div>
    <div class="mt-4">
      <span class="text-xl font-bold">Total: ${{ cartTotal }}</span>
    </div>
    <div class="mt-8">
      <h2 class="text-xl font-semibold mb-2">Your Details</h2>
      <form @submit.prevent="placeOrder">
        <input 
          v-model="userDetails.name" 
          type="text" 
          placeholder="Full Name" 
          class="block w-full mb-4 p-2 border rounded" 
        />
        <input 
          v-model="userDetails.address" 
          type="text" 
          placeholder="Shipping Address" 
          class="block w-full mb-4 p-2 border rounded" 
        />
        <button 
          type="submit" 
          class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">
          Place Order
        </button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  data() {
    return {
      userDetails: {
        name: "",
        address: "",
      },
    };
  },
  computed: {
    ...mapState(["cartItems"]),
    cartTotal() {
      return this.cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
    },
  },
  methods: {
    async placeOrder() {
      try {
        const order = {
          userDetails: this.userDetails,
          items: this.cartItems,
        };
        await this.$store.dispatch("placeOrder", order);
        alert("Order placed successfully!");
        this.$router.push("/");
      } catch (error) {
        console.error("Failed to place order:", error);
      }
    },
    ...mapActions(["placeOrder"]),
  },
};
</script>
