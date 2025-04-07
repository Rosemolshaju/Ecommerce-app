<template>
  <div class="cart">
    <h1 class="text-2xl font-bold mb-4">Shopping Cart</h1>
    <div v-for="item in cartItems" :key="item.id" class="cart-item flex justify-between items-center border-b py-2">
      <div>
        <h2 class="text-lg font-semibold">{{ item.name }}</h2>
        <p>Quantity: {{ item.quantity }}</p>
      </div>
      <span class="text-lg font-semibold">${{ item.price * item.quantity }}</span>
      <button 
        @click="removeFromCart(item.id)" 
        class="bg-red-500 text-white px-2 py-1 rounded">
        Remove
      </button>
    </div>
    <div class="mt-4">
      <span class="text-xl font-bold">Total: ${{ cartTotal }}</span>
      <button class="mt-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">Proceed to Checkout</button>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  computed: {
    ...mapState(["cartItems"]),
    cartTotal() {
      return this.cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
    },
  },
  methods: {
    ...mapActions(["removeFromCart"]),
  },
};
</script>
