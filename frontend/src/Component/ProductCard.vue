<template>
  <div class="product-card border border-gray-300 p-4 rounded-lg">
    <img :src="product.image" alt="Product Image" class="w-full h-48 object-cover rounded-md" />
    <h2 class="text-xl font-bold mt-2">{{ product.name }}</h2>
    <p class="text-gray-700">{{ product.description }}</p>
    <span class="text-lg font-semibold">${{ product.price }}</span>
    <button 
      @click="addToCart(product)" 
      class="mt-2 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
      Add to Cart
    </button>
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  props: ["product"],
  methods: {
    ...mapActions(["addToCart"]),
  },
};
</script>
