#!/usr/bin/env python3
"""
repair_contact_section_structure.py
Replaces the #contact section in all Spanish HTML files with perfectly structured HTML
where contact-left and contact-right are properly closed and placed side-by-side in contact-grid.
"""

import os
import re

BASE = "/Users/deepankarakasajoo/Downloads/Trace's Projects/Family First Legacy/Family1stLegacy"

SPANISH_CONTACT_SECTION = """<section id="contact">
  <div class="container">
    <div class="contact-grid">
      <div class="contact-left">
        <p class="t-label" data-reveal=""><span class="green-dot"></span>Ponte en contacto</p>
        <h2 class="t-h1" data-delay="1" data-reveal="" style="margin-top:16px">Tu legado comienza<br/>con una conversación.</h2>
        <p data-delay="2" data-reveal="">Ya sea que estés protegiendo a tu familia, preparándote para la jubilación, planificando el futuro de tus hijos o construyendo un legado, nuestra meta es brindarte orientación honesta, explicaciones claras y la información que necesitas para tomar decisiones con confianza, sin presión y a tu propio ritmo.</p>

        <div class="contact-trust" data-delay="2" data-reveal="">
          <span class="ct-chip"><svg viewbox="0 0 24 24"><path d="M9 12l2 2 4-4M7.835 4.697a3.42 3.42 0 001.946-.806 3.42 3.42 0 014.438 0 3.42 3.42 0 001.946.806 3.42 3.42 0 013.138 3.138 3.42 3.42 0 00.806 1.946 3.42 3.42 0 010 4.438 3.42 3.42 0 00-.806 1.946 3.42 3.42 0 01-3.138 3.138 3.42 3.42 0 00-1.946.806 3.42 3.42 0 01-4.438 0 3.42 3.42 0 00-1.946-.806 3.42 3.42 0 01-3.138-3.138 3.42 3.42 0 00-.806-1.946 3.42 3.42 0 010-4.438 3.42 3.42 0 00.806-1.946 3.42 3.42 0 013.138-3.138z"></path></svg>Con licencia y asegurados</span>
          <span class="ct-chip"><svg viewbox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7z"></path></svg>Respuesta en 24 horas</span>
          <span class="ct-chip"><svg viewbox="0 0 24 24"><path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>Tu privacidad nos importa</span>
        </div>

        <div class="contact-info-list" data-delay="3" data-reveal="">
          <a class="ci-row" href="mailto:info@family1stlegacy.com">
            <div class="ci-icon">
              <svg viewbox="0 0 24 24"><path d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path></svg>
            </div>
            <div class="ci-body">
              <div class="ci-label">Envíenos un correo electrónico</div>
              <div class="ci-val">info@family1stlegacy.com</div>
            </div>
            <div class="ci-arrow"><svg viewbox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"></path></svg></div>
          </a>
          <a class="ci-row" href="tel:+14696081595">
            <div class="ci-icon">
              <svg viewbox="0 0 24 24"><path d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"></path></svg>
            </div>
            <div class="ci-body">
              <div class="ci-label">Llama o envía un mensaje de texto</div>
              <div class="ci-val">(469) 608-1595</div>
            </div>
            <div class="ci-arrow"><svg viewbox="0 0 24 24"><path d="M5 12h14M12 5l7 7-7 7"></path></svg></div>
          </a>
          <div class="ci-row" style="cursor:default">
            <div class="ci-icon">
              <svg viewbox="0 0 24 24"><path d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"></path><path d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"></path></svg>
            </div>
            <div class="ci-body">
              <div class="ci-label">Área de Servicio</div>
              <div class="ci-val">Área metropolitana de Dallas-Fort Worth, TX y a nivel nacional</div>
            </div>
          </div>
          <div class="ci-row" style="cursor:default">
            <div class="ci-icon">
              <svg viewbox="0 0 24 24"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
            </div>
            <div class="ci-body">
              <div class="ci-label">Horario de oficina</div>
              <div class="ci-val">Lun–Vie: 9 a. m. – 7 p. m. · Sáb: 2 p. m. – 6 p. m.</div>
            </div>
          </div>
        </div>
      </div>

      <div class="contact-right" data-delay="2" data-reveal="">
        <div class="contact-form">
          <div class="cf-tag">Gratis · Sin compromiso</div>
          <div class="cf-heading">Solicitar una consulta</div>
          <div class="cf-sub">Completa el formulario a continuación; nuestra meta es responderte dentro de las próximas 24 horas.</div>
          <form onsubmit="submitForm(event)">
            <div class="form-row">
              <div class="fg">
                <label>Nombre de pila</label>
                <input name="FirstName" placeholder="John" required="" type="text"/>
              </div>
              <div class="fg">
                <label>Apellido</label>
                <input name="LastName" placeholder="Smith" required="" type="text"/>
              </div>
            </div>
            <div class="fg">
              <label>Dirección de correo electrónico</label>
              <input name="Email" placeholder="john@email.com" required="" type="email"/>
            </div>
            <div class="form-row">
              <div class="fg">
                <label>Teléfono</label>
                <input name="Phone" placeholder="(214) 000-0000" type="tel"/>
              </div>
              <div class="fg">
                <label>Estado</label>
                <input name="State" placeholder="Texas" type="text"/>
              </div>
            </div>
            <div class="fg">
              <label>Estoy interesado en</label>
              <select name="Service" required="">
                <option disabled="" selected="" value="">Seleccione un servicio…</option>
                <option>Protección de seguro de vida</option>
                <option>Planificación de jubilación</option>
                <option>Planificación de la educación</option>
                <option>Preservación del patrimonio</option>
                <option>Estrategias de Negocios</option>
                <option>Oportunidad de carrera</option>
                <option>Revisión financiera general</option>
              </select>
            </div>
            <div class="fg">
              <label>Mensaje (opcional)</label>
              <textarea name="Message" placeholder="Cuéntenos sus objetivos o preguntas…"></textarea>
            </div>
            <button class="form-submit" type="submit">Enviar mi solicitud<svg viewbox="0 0 24 24"><line x1="22" x2="11" y1="2" y2="13"></line><polygon points="22 2 15 22 11 13 2 9 22 2"></polygon></svg>
            </button>
            <div class="cf-note">
              <svg viewbox="0 0 24 24"><path d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path></svg>Tu información se maneja con cuidado y se mantiene privada. No vendemos tu información personal.
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>"""

def repair():
    html_files = [f for f in os.listdir(BASE) if f.endswith("_es.html") and not f.startswith("v1") and not f.startswith("old")]

    for fname in html_files:
        fpath = os.path.join(BASE, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            content = f.read()

        # Replace entire section id="contact" ... </section> block cleanly
        new_content = re.sub(
            r'<section id="contact">.*?</section>',
            SPANISH_CONTACT_SECTION,
            content,
            flags=re.DOTALL
        )

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"  ✓ Repaired contact section HTML hierarchy on {fname}")

if __name__ == "__main__":
    print("=== Repairing Contact Section HTML Hierarchy ===")
    repair()
    print("=== Done! ===")
