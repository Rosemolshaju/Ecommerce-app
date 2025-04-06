<template>
  <div class="checkout-page max-w-lg mx-auto">
    <h1 class="text-2xl font-bold mb-4">Order Summary</h1>
    <div v-for="item in cartItems" :key="item.id" class="order-item flex justify-between py-2">
      <span>{{ item.name }} (x{{ item.quantity }})</span>
      <span>${{ item.price * item.quantity }}</span>
    </div>
    <div class="mt-4">
      <span class="text-xl font-bold">Total: ${{ cartTotal }}</span>
    </div>
    <button class="mt-4 bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600">
      Place Order
    </button>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cartItems: [
        { id: 1, name: "Product A", price: 20, quantity: 2 },
        { id: 2, name: "Product B", price: 15, quantity: 1 },
      ],
    };
  },
  computed: {
    cartTotal() {
      return this.cartItems.reduce((total, item) => total + item.price * item.quantity, 0);
    },
  },
};
</script>
