<script lang=ts>
    interface Chart {
        description: string;
        difficulty: string;
        meter: string;
    }

    export let title: string;
    export let subtitle: string;
    export let artist: string;
    export let pack: string;
    export let bpm: string;
    export let charts: Array<Chart>;
    let focusedChart = charts[charts.length - 1];
    let difficultyToColor = {
        "Beginner": "bg-green-400",
        "Easy": "bg-yellow-400",
        "Medium": "bg-orange-400",
        "Hard": "bg-red-400",
        "Challenge": "bg-purple-400",
        "Edit": "bg-grey-400"
    }
</script>
<div class="mx-auto my-1 w-2/3 flex flex-row justify-between border-2 border-black p-1">
    <div class="block w-4/6 p-1 py-1 text-base text-black-700">
        <h1 class="font-bold">{title} <i class="font-normal">{subtitle}</i></h1>
        <div class="flex justify-between">
            <p>{artist}</p>
            <p>BPM: {bpm}</p>
        </div>
        <div class="flex justify-between">
            <p>From: {pack}</p>
            <div class="flex justify-end w-1/6 p-2">
                {#each charts as chart}
                    <div class="flex">
                        <button 
                        class={"w-8 h-8 rounded-md mx-1 " + difficultyToColor[chart.difficulty]}
                        class:selected={focusedChart == chart}
                        on:click={() => focusedChart = chart}
                        >{chart.meter}</button>
                    </div>
                {/each}
            </div>
        </div>
    </div>
    <div class="w-2/6 border-l-2 border-gray-400 p-1">
        <p>{focusedChart.difficulty} {focusedChart.meter}</p>
        <p>{focusedChart.description}</p>
    </div>
</div>
<style>
    .selected {
        @apply border-solid border-black border-2;
    }
</style>