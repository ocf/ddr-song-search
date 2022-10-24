<script>
    import Song from './Song.svelte';
    const promise = fetch('/src/songs_small.json').then(x => x.json());
</script>

<div id="song-list">
    {#await promise}
    <p>waiting...</p>
    {:then packs}
        {#each Object.keys(packs) as packKey}
            {#each packs[packKey] as song}
                <Song pack={packKey} song={song} />
            {/each}
        {/each}
    {/await}
</div>

<style>

    #song-list {
        background-color:black;
        padding: 5px;
        height: calc(100vh * 0.8);
        overflow-y: scroll;
    }

</style>

