<template>
    <div class = "main-grid">
        <p>facts div</p>
        <p>meals div</p>
        <FilterSidebar>

        </FilterSidebar>
    </div>
</template>

<script>
import FilterSidebar from '../FilterSidebar.vue';


export default{
    components: {
        FilterSidebar
    }

}

</script>

<style scoped>
.main-grid {
    display: grid;
    grid-template-columns: 2fr 6fr 3fr;
}

</style>