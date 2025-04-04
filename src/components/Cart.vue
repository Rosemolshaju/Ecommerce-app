<template>
  <div>
    <h3>Your Cart</h3>
    <ul>
      <li v-for="item in cartItems" :key="item.id">
        {{ item.product.name }} - Quantity: {{ item.quantity }}
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      cartItems: []
    };
  },
  methods: {
    async fetchCart() {
      const response = await fetch("http://localhost:8000/cart/?user_id=1");
      this.cartItems = await response.json();
    }
  },
  mounted() {
    this.fetchCart();
  }
};
</script>
