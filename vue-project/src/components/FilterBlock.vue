<template>

    <div class = "filter-div">
        <div class = "icon-div">
            <img src = "../assets/images/filter-icon.png" style = "max-width: 30px"/>
            <p>Filter</p>
        </div>

        <MultiDropdown
            title = "Dining Hall"
            :options = halls
            :forceClose = hallsClosed
            @change = "setHalls"
        ></MultiDropdown>

        <MultiDropdown
            title = "Course"
            :options = times
            :forceClose = timesClosed
            @change = "setTimes"
        ></MultiDropdown>

        <div>
            <img src = "../assets/images/search-icon.png" style = "max-height: 50px" @click="searchRequest">
        </div>

    </div>

    <SingleDropdown
        :options = sorts
        @selected = "setSort"
        @arrow = "chosen.ascending = !chosen.ascending"
    ></SingleDropdown>

</template>

<script>

import MultiDropdown from './MultiDropdown.vue'
import SingleDropdown from './SingleDropdown.vue'
import axios from 'axios'


export default {
    components: {
        MultiDropdown,
        SingleDropdown
    },
    data() {
        return {
            halls: ["Bursley", "East Quad", "Markley", "Mosher Jordan", "North Quad", "South Quad", "Twigs at Oxford"],
            times: ["Breakfast", "Lunch", "Dinner"],
            sorts: ["Nutrition Score", "Calories", "Protein", "Sugars"],

            chosen: {
                halls: [],
                times: [],
                sort: 'Nutrition Score',
                ascending: false
            },
            filteredList: [],

            hallsClosed: false,
            timesClosed: false
        }
    },
    methods: {
        async searchRequest() {
            this.hallsClosed = true
            this.timesClosed = true

            const payload = this.chosen
            await axios.post('http://localhost:5001/filter', payload)
                .then((res) => { this.filteredList = res.data.data })
                .catch((error) => { console.log(error)})
            
            this.$emit('search', this.filteredList)
            this.hallsClosed = false
            this.timesClosed = false

        },
        setHalls (halls) {
            this.chosen.halls = halls

        },
        setTimes (times) {
            this.chosen.times = times
        },
        setSort (sort) {
            this.chosen.sort = sort;
        }
    },
}

</script>


<style>

.filter-div {
    background-color: #313346;
    padding: 20px 40px;
    border-radius: 12px;
    color: white;
    height: 50px;
    font-size: 18px;

    display: flex;
    justify-content: flex-start;
    column-gap: 60px;
}

.icon-div {
    display: flex;
    flex-direction: row;
    column-gap: 10px;
    align-items: center;
}

</style>