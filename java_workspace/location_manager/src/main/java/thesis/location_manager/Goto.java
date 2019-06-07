package thesis.location_manager;

public class Goto {
	
	double orz;
	double orx;
	double ory;
	double orw;
	double posx;
	double posy;
	String tst;
	long latency;
	
	public Goto(){}
	
	public Goto(double orx, double ory,  double orz, double orw, double posx, double posy ,String tst ,long latency) {
		this.orx = orx;
		this.ory = ory;
		this.orz = orz;
		this.orw = orw;
		this.posx = posx;
		this.posy = posy;
		this.tst = tst;
		this.latency = latency;
		
		
	}

	/**
	 * @return the orz
	 */
	public double getOrz() {
		return orz;
	}

	/**
	 * @param orz the orz to set
	 */
	public void setOrz(double orz) {
		this.orz = orz;
	}

	/**
	 * @return the orx
	 */
	public double getOrx() {
		return orx;
	}

	/**
	 * @param orx the orx to set
	 */
	public void setOrx(double orx) {
		this.orx = orx;
	}

	/**
	 * @return the ory
	 */
	public double getOry() {
		return ory;
	}

	/**
	 * @param ory the ory to set
	 */
	public void setOry(double ory) {
		this.ory = ory;
	}

	/**
	 * @return the orw
	 */
	public double getOrw() {
		return orw;
	}

	/**
	 * @param orw the orw to set
	 */
	public void setOrw(double orw) {
		this.orw = orw;
	}

	/**
	 * @return the posx
	 */
	public double getPosx() {
		return posx;
	}

	/**
	 * @param posx the posx to set
	 */
	public void setPosx(double posx) {
		this.posx = posx;
	}

	/**
	 * @return the posy
	 */
	public double getPosy() {
		return posy;
	}

	/**
	 * @param posy the posy to set
	 */
	public void setPosy(double posy) {
		this.posy = posy;
	}

	/**
	 * @return the tst
	 */
	public String getTst() {
		return tst;
	}

	/**
	 * @param tst the tst to set
	 */
	public void setTst(String tst) {
		this.tst = tst;
	}

	/**
	 * @return the latency
	 */
	public long getLatency() {
		return latency;
	}

	/**
	 * @param latency the latency to set
	 */
	public void setLatency(long latency) {
		this.latency = latency;
	}

	

	
}
