<template>

    <div class = "filter-div">
        <div class = "icon-div">
            <img style = "max-width: 30px" src = "../assets/images/filter-icon.png" alt = "filter icon"/>
            <p>Filter</p>
        </div>

        <MultiDropdown 
            title = "Dining Hall"
            :options = halls
        ></MultiDropdown>

        <MultiDropdown
            title = "Meal Time"
            :options = meals
        ></MultiDropdown>

    </div>

</template>

<script>

import MultiDropdown from './MultiDropdown.vue';

export default {
    components: {
        MultiDropdown
    },
    data() {
        return {
            halls: ["South Quad", "Mojo", "Markley"],
            meals: ["Breakfast", "Lunch", "Dinner"]
        }
    }
}

</script>


<style>

.filter-div {
    background-color: #313346;
    padding: 20px 40px;
    border-radius: 12px;
    color: white;
    height: 50px;
    
    display: flex;
    justify-content: flex-start;
    column-gap: 80px;
}

.icon-div {
    display: flex;
    flex-direction: row;
    column-gap: 10px;
    align-items: center;
}
</style>