<template>
  <div class="p-4">
    <div class="mb-3">
      <h1>Upload a screenshot of your loadout to extract the text</h1>
      <p><small>
        <b>Pro tip:</b> Just hit <span class="code">alt+PrintScreen</span> 
        on the game and <span class="code">ctrl+v</span> here
      </small></p>
      <p><small><em>The better the quality, more accurate the result will be</em></small></p>
    </div>

    <figure class="image preview-image">
      <img v-if="url" :src="url">
    </figure>

    <form
      @submit.prevent="submitFile()"
      class="form"
      >
      <div class="file is-link my-4">
        <label class="file-label">
          <input
            @change="onFileChange()"
            class="file-input"
            id="file"
            type="file"
            name="image"
            accept="image/*"
            :disabled="submitting"
            >
          <span class="file-cta">
            <span class="file-icon text-light">
              <font-awesome-icon
                :icon="['fas', 'upload']"
              />
            </span>
            <span class="file-label text-light">
              Upload image
            </span>
          </span>
        </label>
      </div>

      <button 
        class="button is-link"
        type="submit"
        :class="{'is-loading' : submitting} "
        :disabled="!this.url || submitting"
      >
        Send
      </button>
    </form>
    <section class="mt-4">
      <h4>Text extracted:</h4>
      <div class="box">
        {{ output || 'No loadout sent yet' }}
      </div>
    </section>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'IndexPage',

  data() {
    return {
      output: '',
      url: null,
      submitting: false,
      file: null
    }
  },

  methods: {
    onFileChange() {
      const imagefile = document.querySelector("#file");
      this.file = imagefile.files[0]
      this.url = URL.createObjectURL(this.file);
    },
    async submitFile() {
      this.submitting = true;
      const formData = new FormData();

      formData.append("image", this.file);

      try {
        // const { data } = await axios.post('http://localhost:5000', formData)
        const { data } = await axios.post('https://loadout2text.herokuapp.com', formData)
        this.output = data.response
      } catch (e) {
        this.output = 'Something wrong happened, please try again.'
      }
      this.submitting = false;
    },
    getImageFromClipboard(items) {
      const blob = items[0].getAsFile();
      if(blob.type.match('image.*')) {
        this.file = blob;
        this.url = URL.createObjectURL(this.file);
      }
    }
  },

  async beforeMount() {
    document.onpaste = (event) => {
      this.getImageFromClipboard(event.clipboardData.items);
    }
    // Call to wakup the server
    try {
      // await axios.get('http://localhost:5000')
      await axios.get('https://loadout2text.herokuapp.com')
    } catch (e) {
      console.log('The server may be down!')
    }
  }

}
</script>

<style>
html {
  height: 100%;
}

body {
  min-height: 100%;
}

em {
  font-style: italic;
}

.code {
  font-family: monospace;
  font-weight: 600;
  padding: 0 3px;
}

.form {
  display: flex;
  flex-direction: column;
}

.preview-image {
  max-width: 800px;
  max-height: 600px;
  display: flex;
}

.button {
  max-width: 300px;
}
</style>
