<template>
  <div class="product-detail max-w-2xl mx-auto mt-8">
    <img :src="product.image" alt="Product Image" class="w-full h-96 object-cover rounded-md" />
    <h2 class="text-2xl font-bold mt-4">{{ product.name }}</h2>
    <p class="text-gray-700 mt-2">{{ product.description }}</p>
    <div class="text-lg font-semibold mt-4">Price: ${{ product.price }}</div>
    <button 
      @click="addToCart(product)" 
      class="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
      Add to Cart
    </button>
  </div>
</template>

<script>
import api from "../utils/api";
import { mapActions } from "vuex";

export default {
  data() {
    return {
      product: {},
    };
  },
  async created() {
    const productId = this.$route.params.id;
    try {
      const response = await api.get(`/products/${productId}`);
      this.product = response.data;
    } catch (error) {
      console.error("Failed to fetch product:", error);
    }
  },
  methods: {
    ...mapActions(["addToCart"]),
  },
};
</script>
