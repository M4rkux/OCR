<template>
  <div class="p-5">

    <div class="mb-3">
      <h1>Upload a screenshot of your loadout to extract the text</h1>
      <small>The better the quality, the more accurate the result can be</small>
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
    <section class="mt-6">
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
      submitting: false
    }
  },

  computed: {
    file() {
      if (!document) return null
      const imagefile = document.querySelector("#file");
      return imagefile.files[0];
    }
  },

  methods: {
    onFileChange() {
      this.url = URL.createObjectURL(this.file);
    },
    async submitFile() {
      this.submitting = true;
      const formData = new FormData();

      formData.append("image", this.file);


      try {
        const { data } = await axios.post('http://localhost:5000', formData)
        // const { data } = await axios.post('https://loadout2text.herokuapp.com', formData)
        this.output = data.response
      } catch (e) {
        this.output = 'Something wrong happened, please try again.'
      }
      this.submitting = false;
    }
  },

  beforeMount() {
    // Call to wakup the server
    axios.get('http://localhost:5000')
    // axios.get('https://loadout2text.herokuapp.com')
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
