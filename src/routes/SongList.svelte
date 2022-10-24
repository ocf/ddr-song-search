<script>
	import { json } from '@sveltejs/kit';
    import Song from './Song.svelte';
    // const packs = fetch('/src/songs_small.json').then(x => x.json()).then(results => window.myResults = results)
    const promise = fetch('/src/songs_small.json').then(x => x.json());
    // const packKeys = Object.keys(packs).slice(0,2);
</script>

<div>
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


