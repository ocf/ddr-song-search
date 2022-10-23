<script>
    const getBPM = (bpmString) => {
        const regexp = /=\d+\b/g;
        const bpms = [...(bpmString.matchAll(regexp))].map(x => parseInt(x[0].slice(1)));
        if (bpms.length == 1)
            return bpms[0];
        return `${Math.min(...bpms)}–${Math.max(...bpms)}`
    };

    const getDifficulties = (charts) => {
        const difficulties = charts.map(c => [parseInt(c.meter), c.difficulty.toLowerCase()]).sort(
            (a,b) => a[0] > b[0] || (a[0] == b[0] && a[1] == 'edit'));
        return difficulties;
    }

    export let song;
    export let pack;
    const {title, subtitle, artist, charts, bpms} = song;
    const bpm = getBPM(bpms);
    const difficulties = getDifficulties(charts);
    console.log(difficulties);
</script>

<div class='body'>
    <div><span class='title'>{title}</span><span class='subtitle'>{subtitle}</span></div>
    <div class='artist'>{artist}</div>
    <div class='pack'>From pack {pack}</div>
    <div class='bpm'>{bpm}</div>
    <div class='difficulties'>
        {#each difficulties as difficulty}
        <div class={`difficulty-${difficulty[1]} difficulty`}>
            {difficulty[0]}
        </div>
        {/each}
    </div>
</div>

<style>
    .body {
        width: 80%;
        outline: 2px solid black;
    }
    .title {
        font-size: 15px;
    }

    .subtitle {
        margin-left: 10px;
        color: gray;
        font-size: 12px;
    }

    .difficulty-beginner {
        background-color: lightblue;
    }

    .difficulty-easy {
        background-color: lightgreen;
    }

    .difficulty-medium {
        background-color: lightyellow;
    }

    .difficulty-hard {
        background-color: #FFD580;
    }

    .difficulty-challenge {
        background-color: pink;
    }

    .difficulty-edit {
        background-color: gray;
    }

    .difficulties {
        display: flex;
        flex-direction: row;
    }

    div {
        background-color: aliceblue;
        margin: 7px;
        padding: 5px;
	}
</style>
