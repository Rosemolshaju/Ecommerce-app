<template>
  <div class="product-card">
    <img :src="product.image" alt="Product Image" />
    <h2>{{ product.name }}</h2>
    <p>{{ product.description }}</p>
    <span>${{ product.price }}</span>
    <button @click="addToCart(product)">Add to Cart</button>
  </div>
</template>

<script>
export default {
  props: ['product'],
  methods: {
    addToCart(product) {
      // Add product to cart logic
      console.log(`Added ${product.name} to cart!`);
    },
  },
};
</script>

<style>
.product-card {
  border: 1px solid #ddd;
  padding: 10px;
  margin: 10px;
}
</style>
