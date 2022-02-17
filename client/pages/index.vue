<template>
  <div class="m-5">

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
      <div class="file my-4">
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
            <span class="file-icon">
              <font-awesome-icon
                :icon="['fas', 'upload']"
              />
            </span>
            <span class="file-label">
              Upload image
            </span>
          </span>
        </label>
      </div>

      <button 
        class="button is-primary"
        type="submit"
        :disabled="!this.url || submitting"
      >
        <span v-if="!submitting">Enviar</span>

        <font-awesome-icon
          v-else
          :icon="['fas', 'spinner']"
          pulse
        />
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

  methods: {
    onFileChange() {
      const imagefile = document.querySelector("#file");
      this.url = URL.createObjectURL(imagefile.files[0]);
    },
    async submitFile() {
      this.submitting = true;
      const formData = new FormData();
      const imagefile = document.querySelector("#file");

      formData.append("image", imagefile.files[0]);

      const { data } = await axios.post("http://localhost:5000", formData)
      // const { data } = await axios.post("https://loadout2text.herokuapp.com", formData)
      this.output = data.response
      this.submitting = false;
    }
  }
}
</script>

<style>
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
