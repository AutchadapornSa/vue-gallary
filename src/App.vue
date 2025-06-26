<template>
  <main class="container mx-auto p-4">
    <h1 class="text-3xl font-bold mb-4">Gallery</h1>
    <SearchBar v-model:searchTerm='searchTerm' />
    <GalleryGrid :searchTerm="searchTerm" @update:searchTerm="searchTerm = $event" />
  </main>
</template>

<script setup>
import { ref } from 'vue'
import GalleryGrid from './components/GalleryGrid.vue'
import SearchBar from './components/SearchBar.vue'

const searchTerm = ref('')
</script>