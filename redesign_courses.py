import re

html_file = 'courses.html'

with open(html_file, 'r', encoding='utf-8') as f:
    content = f.read()

# We want to replace the whole <div class="row g-5"> block inside "Course List Section"
# It starts around line 62 and ends around 178

new_cards = """      <div class="row g-5">
        <!-- Beginner Courses -->
        <div class="col-lg-6" data-aos="fade-up">
          <div class="card bg-color border border-secondary shadow-lg h-100 p-4 rounded-4 position-relative overflow-hidden transition-hover" style="z-index: 1;">
            <div class="position-absolute top-0 end-0 p-3 opacity-25" style="z-index: -1;">
              <i class="bi bi-shield-check" style="font-size: 8rem;"></i>
            </div>
            <div class="d-flex align-items-center mb-4 pb-3 border-bottom border-secondary">
              <div class="d-flex align-items-center justify-content-center bg-dark text-secondary fw-bold rounded-3 me-3 shadow" style="width: 55px; height: 55px; font-size: 1.5rem;">
                01
              </div>
              <div>
                <h3 class="fw-bold mb-0 text-uppercase" style="letter-spacing: 1px;">Fundamentals</h3>
              </div>
              <span class="badge bg-secondary text-dark ms-auto px-3 py-2 rounded-pill fw-bold">Beginner</span>
            </div>
            <p class="text-muted mb-4">Perfect for first-time owners or those looking to refresh their basic safety and handling skills.</p>
            
            <div class="d-flex flex-column gap-3 mt-auto">
              <div class="p-3 bg-dark rounded border border-secondary transition-hover" style="cursor: pointer;">
                <div class="d-flex justify-content-between align-items-start mb-2">
                  <h6 class="fw-bold text-white mb-0">Intro to Handguns</h6>
                  <span class="badge bg-secondary text-dark rounded-pill fw-bold fs-6">$125</span>
                </div>
                <small class="text-white-50"><i class="bi bi-clock me-1"></i> 4 Hours &bull; Classroom + Range</small>
              </div>
              
              <div class="p-3 bg-dark rounded border border-secondary transition-hover" style="cursor: pointer;">
                <div class="d-flex justify-content-between align-items-start mb-2">
                  <h6 class="fw-bold text-white mb-0">Basic Rifle Marksmanship</h6>
                  <span class="badge bg-secondary text-dark rounded-pill fw-bold fs-6">$150</span>
                </div>
                <small class="text-white-50"><i class="bi bi-clock me-1"></i> 6 Hours &bull; Classroom + Range</small>
              </div>
            </div>
          </div>
        </div>

        <!-- Intermediate Courses -->
        <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">
          <div class="card bg-color border border-secondary shadow-lg h-100 p-4 rounded-4 position-relative overflow-hidden transition-hover" style="z-index: 1;">
            <div class="position-absolute top-0 end-0 p-3 opacity-25" style="z-index: -1;">
              <i class="bi bi-crosshair" style="font-size: 8rem;"></i>
            </div>
            <div class="d-flex align-items-center mb-4 pb-3 border-bottom border-secondary">
              <div class="d-flex align-items-center justify-content-center bg-dark text-secondary fw-bold rounded-3 me-3 shadow" style="width: 55px; height: 55px; font-size: 1.5rem;">
                02
              </div>
              <div>
                <h3 class="fw-bold mb-0 text-uppercase" style="letter-spacing: 1px;">Defensive</h3>
              </div>
              <span class="badge bg-primary text-white ms-auto px-3 py-2 rounded-pill fw-bold" style="background-color: var(--primary-color) !important;">Intermediate</span>
            </div>
            <p class="text-muted mb-4">Take your skills to the next level with dynamic drills, drawing from a holster, and rapid target acquisition.</p>
            
            <div class="d-flex flex-column gap-3 mt-auto">
              <div class="p-3 bg-dark rounded border border-secondary transition-hover" style="cursor: pointer;">
                <div class="d-flex justify-content-between align-items-start mb-2">
                  <h6 class="fw-bold text-white mb-0">Concealed Carry CCW</h6>
                  <span class="badge bg-secondary text-dark rounded-pill fw-bold fs-6">$180</span>
                </div>
                <small class="text-white-50"><i class="bi bi-clock me-1"></i> 8 Hours &bull; Certification Included</small>
              </div>
              
              <div class="p-3 bg-dark rounded border border-secondary transition-hover" style="cursor: pointer;">
                <div class="d-flex justify-content-between align-items-start mb-2">
                  <h6 class="fw-bold text-white mb-0">Defensive Pistol I</h6>
                  <span class="badge bg-secondary text-dark rounded-pill fw-bold fs-6">$200</span>
                </div>
                <small class="text-white-50"><i class="bi bi-clock me-1"></i> 6 Hours &bull; Range Only</small>
              </div>
            </div>
          </div>
        </div>

        <!-- Advanced Courses -->
        <div class="col-lg-6" data-aos="fade-up">
          <div class="card bg-color border border-secondary shadow-lg h-100 p-4 rounded-4 position-relative overflow-hidden transition-hover" style="z-index: 1;">
            <div class="position-absolute top-0 end-0 p-3 opacity-25" style="z-index: -1;">
              <i class="bi bi-lightning-charge" style="font-size: 8rem;"></i>
            </div>
            <div class="d-flex align-items-center mb-4 pb-3 border-bottom border-secondary">
              <div class="d-flex align-items-center justify-content-center bg-dark text-secondary fw-bold rounded-3 me-3 shadow" style="width: 55px; height: 55px; font-size: 1.5rem;">
                03
              </div>
              <div>
                <h3 class="fw-bold mb-0 text-uppercase" style="letter-spacing: 1px;">Tactical</h3>
              </div>
              <span class="badge text-white ms-auto px-3 py-2 rounded-pill fw-bold" style="background-color: #8c2a2a;">Advanced</span>
            </div>
            <p class="text-muted mb-4">High-stress scenarios, low-light training, and advanced movement techniques for experienced shooters.</p>
            
            <div class="d-flex flex-column gap-3 mt-auto">
              <div class="p-3 bg-dark rounded border border-secondary transition-hover" style="cursor: pointer;">
                <div class="d-flex justify-content-between align-items-start mb-2">
                  <h6 class="fw-bold text-white mb-0">Low-Light Engagements</h6>
                  <span class="badge bg-secondary text-dark rounded-pill fw-bold fs-6">$225</span>
                </div>
                <small class="text-white-50"><i class="bi bi-clock me-1"></i> 4 Hours &bull; Evening Session</small>
              </div>
              
              <div class="p-3 bg-dark rounded border border-secondary transition-hover" style="cursor: pointer;">
                <div class="d-flex justify-content-between align-items-start mb-2">
                  <h6 class="fw-bold text-white mb-0">Urban Carbine Tactics</h6>
                  <span class="badge bg-secondary text-dark rounded-pill fw-bold fs-6">$250</span>
                </div>
                <small class="text-white-50"><i class="bi bi-clock me-1"></i> 8 Hours &bull; Outdoor Range</small>
              </div>
            </div>
          </div>
        </div>

        <!-- Specialized Programs -->
        <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">
          <div class="card bg-color border border-secondary shadow-lg h-100 p-4 rounded-4 position-relative overflow-hidden transition-hover" style="z-index: 1;">
            <div class="position-absolute top-0 end-0 p-3 opacity-25" style="z-index: -1;">
              <i class="bi bi-star" style="font-size: 8rem;"></i>
            </div>
            <div class="d-flex align-items-center mb-4 pb-3 border-bottom border-secondary">
              <div class="d-flex align-items-center justify-content-center bg-dark text-secondary fw-bold rounded-3 me-3 shadow" style="width: 55px; height: 55px; font-size: 1.5rem;">
                <i class="bi bi-star-fill text-secondary"></i>
              </div>
              <div>
                <h3 class="fw-bold mb-0 text-uppercase" style="letter-spacing: 1px;">Specialized</h3>
              </div>
              <span class="badge text-dark ms-auto px-3 py-2 rounded-pill fw-bold" style="background-color: #d4a373;">Private</span>
            </div>
            <p class="text-muted mb-4">One-on-one coaching and specialized programs for competitors or specialized units.</p>
            
            <div class="d-flex flex-column gap-3 mt-auto">
              <div class="p-3 bg-dark rounded border border-secondary transition-hover" style="cursor: pointer;">
                <div class="d-flex justify-content-between align-items-start mb-2">
                  <h6 class="fw-bold text-white mb-0">Private Instructor Session</h6>
                  <span class="badge bg-secondary text-dark rounded-pill fw-bold fs-6">$90/hr</span>
                </div>
                <small class="text-white-50"><i class="bi bi-clock me-1"></i> Hourly &bull; Customized</small>
              </div>
              
              <div class="p-3 bg-dark rounded border border-secondary transition-hover" style="cursor: pointer;">
                <div class="d-flex justify-content-between align-items-start mb-2">
                  <h6 class="fw-bold text-white mb-0">Competition Prep (USPSA/IDPA)</h6>
                  <span class="badge bg-secondary text-dark rounded-pill fw-bold fs-6">$350</span>
                </div>
                <small class="text-white-50"><i class="bi bi-clock me-1"></i> 2-Day Clinic &bull; Stage Breakdown</small>
              </div>
            </div>
          </div>
        </div>
      </div>"""

# Replace the block
pattern = re.compile(r'<div class="row g-5">.*?<!-- Course Calendar -->', re.DOTALL)
content = pattern.sub(new_cards + '\n    </div>\n  </section>\n\n  <!-- Course Calendar -->', content)

with open(html_file, 'w', encoding='utf-8') as f:
    f.write(content)

print("Redesigned courses section.")
