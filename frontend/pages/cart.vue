<template>
  <div class="cart max-w-3xl mx-auto mt-8">
    <h1 class="text-2xl font-bold mb-4">Your Shopping Cart</h1>
    <div v-if="cartItems.length === 0">
      <p>Your cart is empty.</p>
    </div>
    <div v-else>
      <div v-for="item in cartItems" :key="item.id" class="border-b py-4">
        <div class="flex justify-between items-center">
          <div>
            <h2 class="text-lg font-semibold">{{ item.name }}</h2>
            <p>Quantity: {{ item.quantity }}</p>
          </div>
          <span class="text-lg font-semibold">${{ item.price * item.quantity }}</span>
        </div>
      </div>
      <div class="mt-4">
        <span class="text-xl font-bold">Total: ${{ cartTotal }}</span>
        <button 
          @click="goToCheckout" 
          class="mt-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">
          Proceed to Checkout
        </button>
      </div>
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
    goToCheckout() {
      this.$router.push("/checkout");
    },
    ...mapActions(["removeFromCart"]),
  },
};
</script>
