<script lang=ts>
    const getBPM = (bpmString) => {
        if (bpmString == null)
            return '';
        const regexp = /=\d+\b/g;
        const bpms = [...(bpmString.matchAll(regexp))].map(x => parseInt(x[0].slice(1)));
        if (bpms.length == 1)
            return bpms[0];
        return `${Math.min(...bpms)}–${Math.max(...bpms)}`
    };

    const diffucultySort = (a, b) => {
        a.meter = parseInt(a.meter);
        b.meter = parseInt(b.meter)
        if(a.meter == b.meter) {
            return a['difficulty'] == 'Edit'? 1 : -1;
        }
        return a.meter - b.meter;
    }

    export let song: object;
    export let pack: string;
    // let title: string;
    // let bpms: string;
    // let subtitle: string;
    // let artist: string;
    // let charts: Array<object>;
    let {title, bpms, subtitle, artist, charts} = song;
    const bpm = getBPM(bpms);
    charts.sort(diffucultySort);
    let focusedChart = charts[0];

    function changeChart(chart) : void {
        focusedChart = chart;
    }
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
                        <button class="{difficultyToColor[chart.difficulty]} w-8 h-8 rounded-md mx-1"on:click={changeChart} value={chart}>
                            {chart.meter}
                        </button>
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