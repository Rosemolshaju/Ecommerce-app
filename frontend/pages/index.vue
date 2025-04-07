<template>
  <div class="homepage">
    <h1 class="text-3xl font-bold mb-4">Welcome to Our Store</h1>
    <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4">
      <ProductCard v-for="product in products" :key="product.id" :product="product" />
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex";
import ProductCard from "../Component/ProductCard.vue";

export default {
  components: {
    ProductCard,
  },
  computed: {
    ...mapState(["products"]),
  },
  created() {
    this.fetchProducts();
  },
  methods: {
    ...mapActions(["fetchProducts"]),
  },
};
</script>
