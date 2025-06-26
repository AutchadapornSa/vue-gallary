<template>
    <div class="break-inside-avoid overflow-hidden rounded shadow-lg mb-4">
      <img :src="image.url" alt="Image" class="w-full object-cover" />
      <div class="p-2 flex flex-wrap gap-1">
        <span
          v-for="tag in image.hashtags"
          :key="tag"
          @click="$emit('tag-click', tag)"
          class="text-blue-500 text-xs bg-blue-100 px-2 py-1 rounded cursor-pointer hover:bg-blue-200"
        >
          {{ tag }}
        </span>
      </div>
    </div>
  </template>
  
  <script setup>
    defineProps({ image: Object })
    defineEmits(['tag-click'])
  </script>
  