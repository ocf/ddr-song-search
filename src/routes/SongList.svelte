<script>
    import Song from './Song.svelte';
    import packs from '../songs_small.json';
    let packKeys = Object.keys(packs).slice(0,2);
</script>

<div>
    {#each packKeys as packKey}
        {#each packs[packKey] as song}
        <Song pack={packKey} song={song} />
        {/each}
    {/each}
</div>


