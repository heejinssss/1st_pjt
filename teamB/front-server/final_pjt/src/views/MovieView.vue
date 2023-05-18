<template>
  <div>
  <h1>오늘 영화 어때요?</h1>
  <MovieList/>
  </div>
</template>

<script>
import MovieList from '@/components/MovieList.vue'

export default {
  name: 'MovieView',
  components: {
    MovieList
  },
  computed: {

  },
  created() {
    this.getMovies()
  },
  methods: {
    getMovies() {
      this.$store.dispatch('getMovies')
    }
  }
}
</script>

<style>

</style>