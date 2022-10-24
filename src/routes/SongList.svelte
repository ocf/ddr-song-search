<script>
    import Page from './+page.svelte';
	import Song from './Song.svelte';
    import SongRow from './SongRow.svelte';
    const promise = fetch('/src/songs_small.json').then(x => x.json());
</script>


<div id="song-list">
    {#await promise}
    <p>waiting...</p>
    {:then packs}
        {#each Object.keys(packs) as packKey}
            {#each packs[packKey] as song}
                <SongRow pack={packKey} song={song}/>
            {/each}
        {/each}
    {/await}
</div>

<style>

    #song-list {
        padding: 5px;
        height: calc(100vh * 0.8);
        overflow-y: scroll;
    }

</style>

