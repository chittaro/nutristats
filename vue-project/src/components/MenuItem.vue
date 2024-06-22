<template>
    <div class = "item-div">
        <div class = "title-div">
            <div class = "circle-div">
                <p class = "num">{{ index + 1 }}</p>
            </div>
            <p class="bold"> {{ food }}</p>
        </div>

        <p>Protein: <span class = "bold"> {{ protein }} </span></p>

        <img src = "../assets/images/arrow-down-blue.png" style = "max-height: 20px;"/>
    </div>
</template>

<script>

export default {
    props: {
        food: String,
        index: Number,
        protein: Number
    },
}

</script>

<style>

.num {
    font-size: 15px;
    color: white;
    font-family: "Inter-Bold";
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
    padding: 40px 30px;
    font-size: 25px;

    display: grid;
    grid-template-columns: 5fr 5fr 1fr;
    align-items: center;
}

</style>