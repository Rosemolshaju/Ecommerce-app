<template>
  <div>
    <div v-for="product in products" :key="product.id">
      <h3>{{ product.name }}</h3>
      <p>{{ product.description }}</p>
      <p>${{ product.price }}</p>
      <button @click="addToCart(product.id)">Add to Cart</button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      products: []
    };
  },
  methods: {
    async fetchProducts() {
      const response = await fetch("http://localhost:8000/products/");
      this.products = await response.json();
    },
    async addToCart(productId) {
      await fetch("http://localhost:8000/cart/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ user_id: 1, product_id: productId, quantity: 1 })
      });
    }
  },
  mounted() {
    this.fetchProducts();
  }
};
</script>
