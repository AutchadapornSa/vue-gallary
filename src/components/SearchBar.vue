<template>
    <div class="my-4">
      <input
        type="text"
        v-model="inputValue"
        @input="$emit('update:searchTerm', inputValue)"
        placeholder="Search by hashtag..."
        class="w-full border p-2 rounded"
      />
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  const inputValue = ref('')
  </script>