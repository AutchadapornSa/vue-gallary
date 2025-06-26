<template>
    <div>
      <div class="columns-1 sm:columns-2 md:columns-3 lg:columns-4 gap-4 space-y-4">
        <ImageCard
          v-for="img in displayedImages"
          :key="img.id"
          :image="img"
          @tag-click="handleTagClick"
        />
      </div>
      <div ref="sentinel" class="h-4"></div>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, watch, computed } from 'vue'
  import { images } from '../mockData'
  import ImageCard from './ImageCard.vue'
  
  const props = defineProps({ searchTerm: String })
  const emit = defineEmits(['update:searchTerm'])
  
  const handleTagClick = (tag) => {
    emit('update:searchTerm', tag)
  }
  
  const imagesFiltered = computed(() => {
    if (!props.searchTerm) return images
    return images.filter(img =>
      img.hashtags.some(tag => tag.toLowerCase().includes(props.searchTerm.toLowerCase()))
    )
  })
  
  const displayedImages = ref([])
  const currentPage = ref(0)
  const pageSize = 4
  const sentinel = ref(null)
  
  const loadMore = () => {
    const start = currentPage.value * pageSize
    const end = start + pageSize
    displayedImages.value.push(...imagesFiltered.value.slice(start, end))
    currentPage.value++
  }
  
  onMounted(() => {
    loadMore()
    const observer = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) loadMore()
    })
    observer.observe(sentinel.value)
  })
  
  watch(imagesFiltered, () => {
    displayedImages.value = []
    currentPage.value = 0
    loadMore()
  })
  </script>