<template>
  <div class="homepage">
    <h1 class="text-3xl font-bold mb-4">Welcome to the Store</h1>
    <div class="product-grid grid grid-cols-1 md:grid-cols-3 gap-4">
      <ProductCard 
        v-for="product in products" 
        :key="product.id" 
        :product="product" 
      />
    </div>
  </div>
</template>

<script>
import ProductCard from "../components/ProductCard.vue";

export default {
  components: {
    ProductCard,
  },
  data() {
    return {
      products: [
        { id: 1, name: "Product A", description: "Description A", price: 20, image: "image-a.jpg" },
        { id: 2, name: "Product B", description: "Description B", price: 15, image: "image-b.jpg" },
        
        { id: 8, name: "Product A", description: "Description A", price: 20, image: "image-a.jpg" },
        { id: 7, name: "Product A", description: "Description A", price: 20, image: "image-a.jpg" },
        { id: 6, name: "Product A", description: "Description A", price: 20, image: "image-a.jpg" },
        { id: 3, name: "Product A", description: "Description A", price: 20, image: "image-a.jpg" },
        { id: 4, name: "Product A", description: "Description A", price: 20, image: "image-a.jpg" },
        { id: 5, name: "Product A", description: "Description A", price: 20, image: "image-a.jpg" },
      ],
    };
  },
};
</script>
