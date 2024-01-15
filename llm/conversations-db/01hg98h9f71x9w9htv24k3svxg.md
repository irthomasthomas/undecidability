**Prompt:**


**Response:**
package com.example.teamworkus.data.model

import android.os.Parcelable
import kotlinx.parcelize.Parcelize

@Parcelize
data class Members(
    val id: Int,
    val avatar: String,
    val fullName: String,
    val email: String,
    val phone: String,
    val address: String,
    val dateOfBirth: String,
    val gender: String,
    val team: String,
    val status: String,
    val role: String,
    val notifications: Boolean,
    val project: String,
    val project2: String,
    val project3: String,
    val project4: String,
    val project5: String,
    val project6: String,
    val project7: String,
    val project8: String,
    val project9: String,
    val project10: String
): Parcelable

<details><summary>Metadata</summary>

- Duration: 2350 ms
- Datetime: 2023-11-27T20:46:32.121269
- Model: gpt-3.5-turbo-instruct

</details>

**Options:**
```json
{"temperature": 0.7}
```

