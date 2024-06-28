<template>
    <div class = "item-div">
        <div class = "title-div">
            <div class = "circle-div">
                <p class = "num">{{ index + 1 }}</p>
            </div>
            <div class = "title-list-div">
                <p class="bolder"> {{ data.Menu_Item }}</p>
                <div class = "item-subdiv">
                        
                    <p> <span class = "bold">Dining Hall:</span> {{ getHall }}</p>
                    <p> <span class = "bold">Course:</span> {{ data.Course }} </p>
                    
                </div>
            </div>
        </div>

        <p>Score: <span class = "bold"> {{ data.Nutrition_Score }} </span></p>

        <img src = "../assets/images/arrow-down-blue.png" style = "max-height: 20px;"/>
    </div>
</template>

<script>

export default {
    props: {
        data: Object,
        index: Number,
    },
    computed: {
        getHall() {
            let str = this.data.Dining_Hall
            str = str.split("-")
            for (let i = 0; i < str.length; i++){
                str[i] = str[i][0].toUpperCase() + str[i].slice(1)
            }
            return str.join(" ")

        }
    }
}

</script>

<style>

.num {
    font-size: 15px;
    color: white;
    font-family: "Inter-ExtraBold";
}

.circle-div {
    background-color: #3C3F56;
    border-radius: 50%;
    display: grid;
    justify-content: center;
    align-items: center;
    width: 40px;
    height: 40px;
}

.title-div {
    display: grid;
    grid-template-columns: 1fr 12fr;
    align-items: center;
    gap: 20px;
}

.item-div {
    background-color: #CFD8E1;
    border: 1px solid #3C3F56;
    border-radius: 25px;
    padding: 20px 30px;
    font-size: 25px;

    display: grid;
    grid-template-columns: 5fr 5fr 1fr;
    align-items: center;
}

.title-list-div {
    display: grid;
    grid-template-rows: 1fr 1fr;
    align-items: center;
    gap: 5px;
}

.item-subdiv {
    display: grid;
    gap: 5px;
    font-size: 15px;
}

</style>