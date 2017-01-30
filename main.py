#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar
import cgi
def landing_page(content):
	header = "<h2>Web Caesar</h2>"
	label1= "<label>Rotate by:</label>"
	r_amount = label1+"<br>"+"<input type ='number' name ='rotate'/>"
	label2="<label>Type message:</label>"
	textarea = label2+"<br>"+"<textarea name='message'>"+content+ "</textarea>"
	submit = "<input type='submit'/>"
	form = "<form method='post'>"+r_amount+"<br>"+textarea+"<br>"+submit
	content = header+form
	return content



class MainHandler(webapp2.RequestHandler):
    def get(self):
    	content = landing_page("")
        self.response.write(content)
    def post(self):
    	message = self.request.get("message")
    	rotate = int(self.request.get("rotate"))
    	enc_message = caesar.encrypt(message, rotate)
    	esc_message = cgi.escape(enc_message)
    	content = landing_page(esc_message)
    	self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
