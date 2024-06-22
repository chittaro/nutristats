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

    <div class = "sort">
        <p>Sort By: <span class = "bold">{{ sort }}</span></p>
        <img src = "../assets/images/filled-down-icon.png" style = "max-height: 15px"/>
    </div>

</template>

<script>

import MultiDropdown from './MultiDropdown.vue'
import axios from 'axios'


export default {
    components: {
        MultiDropdown
    },
    data() {
        return {
            halls: ["Bursley", "East Quad", "Markley", "Mosher Jordan", "North Quad", "South Quad", "Twigs at Oxford"],
            times: ["Breakfast", "Lunch", "Dinner"],
            sort: 'Protein',

            chosen: {
                halls: [],
                times: [],
                sort: 'Protein'
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
                    
            const payload = { halls: this.chosen.halls, times: this.chosen.times, sort: this.chosen.sort } 
            await axios.post('http://localhost:5001/filter', payload)
                .then((res) => { this.filteredList = res.data.data })
                .catch((error) => {console.log(error)})
            
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

.sort {
    padding: 20px 40px;
    color: #313346;

    display: flex; flex-direction: row;
    align-items: center;
    column-gap: 7px;
}
</style>