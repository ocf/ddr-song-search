<script>
    import Song from './Song.svelte';
    import allSongs from '../songs.json';
	import Page from './+page.svelte';
    let songKeys = Object.keys(allSongs);
</script>

<div>
    {#each songKeys as songKey}
    <Song difficulties={allSongs[songKey]} />
    {/each}
</div>


